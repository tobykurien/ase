require 'scoring'
require 'marking'

class AssignmentsController < ApplicationController
  before_filter :checkIfLoggedIn!, :except => [:login]
  
  # GET /assignments
  # GET /assignments.json
  def index
    @assignments = Assignment.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @assignments }
    end
  end

  # GET /assignments/1
  # GET /assignments/1.json
  def show
    @assignment = Assignment.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @assignment }
    end
  end

  # GET /assignments/new
  # GET /assignments/new.json
  def new
    @assignment = Assignment.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @assignment }
    end
  end

  # GET /assignments/1/edit
  def edit
    @assignment = Assignment.find(params[:id])
  end

  # POST /assignments
  # POST /assignments.json
  def create
    @assignment = Assignment.new(params[:assignment])

    respond_to do |format|
      if @assignment.save
        format.html { redirect_to @assignment, notice: 'Assignment was successfully created.' }
        format.json { render json: @assignment, status: :created, location: @assignment }
      else
        format.html { render action: "new" }
        format.json { render json: @assignment.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /assignments/1
  # PUT /assignments/1.json
  def update
    @assignment = Assignment.find(params[:id])

    respond_to do |format|
      if @assignment.update_attributes(params[:assignment])
        format.html { redirect_to @assignment, notice: 'Assignment was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @assignment.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /assignments/1
  # DELETE /assignments/1.json
  def destroy
    @assignment = Assignment.find(params[:id])
    @assignment.destroy

    respond_to do |format|
      format.html { redirect_to assignments_url }
      format.json { head :no_content }
    end
  end
  
  # PUT /assignments/start  
  def changestate
    @assignment = Assignment.find(params[:id])
    @assignment.state = params[:newstate]

    redirected = false            
    if(@assignment.save)
       case @assignment.state
          when "BUSY"
             @assignment.startdatetime = Time.now
             @assignment.save
          when "MARKING"
             Marking.new.populateMarking @assignment 
          when "GRADING"
             Marking.new.doscoring @assignment 
             redirect_to grading_assignment_url, notice: 'Grading successfully updated'
             redirected = true            
          when "COMPLETE"
             # do nothing
              
       end
    
       redirect_to assignments_url, notice: 'State successfully updated' unless redirected
    else   
       redirect_to assignments_url, notice: 'Could not update the state'
    end  
  end
  
  def markedprogress
     assignment_id = params[:assignment_id]
     @markprogress  = EssayEval.select("studentname, count(score1) marked, count(1) total").where(:assignment_id => 1).group("studentname")
  end
  
  def grading
    @assignment = Assignment.find(params[:id])
    @sorted = Essay.where({:assignment_id => @assignment.id}).order({:score => :asc}).to_a
    @bottom = @sorted[0]
    
    @top = @sorted[@sorted.count-1]
    
  end
  
  def update_grading
     updategrade()
     redirect_to assignments_url, notice: 'Grading successfully updated'
  end
  
  def updategrade()
    assignment_id = (params["id"]).to_i
    sorted = Essay.where({:assignment_id => assignment_id}).order({:score => :asc})

    bottom = sorted[0]    
    top = sorted[sorted.count-1]
    
    bottom_grade = 40.0 
    bottom_grade = params['bottom_grade'].to_f if params.keys.include? 'bottom_grade'

    top_grade = 80.0 
    top_grade = params['top_grade'].to_f if params.keys.include? 'top_grade'


    sorted.each do |essay|
       essay.grade = (essay.score - bottom.score) / (top.score-bottom.score) * (top_grade - bottom_grade) + bottom_grade
       essay.save! 
    
    end
    
  end
   
  def checkIfLoggedIn!
      if session.has_key? :admin and not session[:admin].nil? then
           return true
      else      
           redirect_to admin_login_url
           return false
      end
  end 


  def login 
      if params[:admin] then
          if params[:admin] == APP_CONFIG['password']
            session[:admin] = params[:admin]
            redirect_to assignments_url
          end  
      end    
      
  end
  

end


