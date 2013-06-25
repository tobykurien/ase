require 'scoring'

class AssignmentsController < ApplicationController
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

    if(@assignment.save)
       case @assignment.state
          when "BUSY"
             @assignment.startdatetime = Date.current
             @assignment.save
          when "MARKING"
             populateMarking @assignment 
          when "COMPLETE"
             doscoring @assignment             
       end
    
       redirect_to assignments_url, notice: 'State successfully updated'
    else   
       redirect_to assignments_url, notice: 'Could not update the state'
    end  
  end
  
  def markedprogress
     assignment_id = params[:assignment_id]
     @markprogress  = EssayEval.select("studentname, count(score1) marked, count(1) total").where(:assignment_id => 1).group("studentname")
  end
    
  def populateMarking(assignment)
  
      EssayEval.where(:assignment_id => assignment.id).delete_all
      essays = assignment.essays
      essayCount = essays.length

      repetitions = 3
      maxCombinations = factorial(essayCount)/factorial(essayCount-2)/factorial(2)
      if maxCombinations< essayCount*repetitions then
         repetitions = (maxCombinations / essayCount).floor.to_i
      end   
      pairs = assignPairs(essayCount, repetitions)   
      essayCount.times.each do |i|
         repetitions.times.each do |j|
            index = i*repetitions+j
            
            ee = EssayEval.new
            ee.essay1_id = essays[pairs[index][0]].id
            ee.essay2_id = essays[pairs[index][1]].id
            ee.studentname = essays[i].studentname
            ee.assignment_id = assignment.id
            ee.save
         end
      end   
     
  end
  
  def assignPairs(essaysCount, numberToSelect)
    result = []
    essayIndex = 0

    while essayIndex < essaysCount do
        numberIndex = 0
        while numberIndex < numberToSelect do
            a = rand(essaysCount)
            b = rand(essaysCount)
            if not (result.include? [a,b]) and not (result.include? [b,a]) and not a==b and not a==essayIndex and not b==essayIndex then
                result.append([a,b])
                numberIndex += 1
            end    
        end        
        essayIndex += 1
    end    
    return result
  end  
  
  def factorial(n)
    n.zero? ? 1 : n * factorial(n - 1)
  end
  
  def doscoring(assignment)
    essays = Essay.where(:assignment_id => assignment).all
    ids = essays.map {|i| i['id'] }
  
    essay_evals = EssayEval.where(:assignment_id => assignment).all
    a = Matrix.zero(essay_evals.count)
    
    essay_evals.each do |i|
      row = ids.index(i['essay1_id'])
      col = ids.index(i['essay2_id']) 
      s1 = i['score1'] 
      s2 = i['score2']
      s1 = 0.5 if s1.nil?
      s2 = 0.5 if s2.nil?
      a[row,col] = s1
      a[col,row] = s2
    end
    
    puts a
    c = colley(a)
    puts c
    c1 = standardize(c)
    puts c1

    essays.each do |e|
      e.score = c1[0,ids.index(e['id'])]
      e.grade = nil
      e.save!
    end
  
  end
  
end

class MarkProgress
   attr_accessor :studentname, :pairsmarked, :total
end
