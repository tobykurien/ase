class HomeController < ApplicationController
  before_filter :checkIfLoggedIn!, :except => [:login,:logout]

  def index
  end
  
  def student
      
      @student = session[:username]   
      @assignment = Assignment.current_assignment
      if(@assignment != nil) then
          case @assignment.state
             when "BUSY"
                 @essay = @assignment.essays.where(:studentname => @student).first
                 if @essay == nil 
                     @essay = @assignment.essays.new
                 end    
                 @form_from_state = 'enter'
                 endtime = @assignment.startdatetime + @assignment.duration*60
                 @timeremaining = (endtime - Time.now).to_i
                 puts @timeremaining
                 @timeremaining = 0 if @timeremaining < 0
             when "MARKING"
                 evals = EssayEval.where(:studentname => @student)
                 @mark_index = 0
                 @mark_index = params[:mark_index].to_i+1 unless params[:mark_index].nil?
                 if @mark_index >= evals.length 
                    @form_from_state = 'done_marking' 
                 else    
                   @essayeval = evals[@mark_index]
                   unless @essayeval.nil? 
                     @score = @essayeval.score1.nil? ? 0.5 : @essayeval.score1
                     @essay1 = Essay.find(@essayeval.essay1_id)
                     @essay2 = Essay.find(@essayeval.essay2_id)                 
                     @form_from_state = 'mark'         
                   else   
                     throw "Could not find essays to evaluate for student:"+@student.to_s
                   end
                 end  
          end   
      else
          @form_from_state = 'list'
          @essays = Essay.where(:studentname => @student).order("created_at DESC")      
      end
  end
  
  def save    
    @essay = Essay.find(params[:id]) rescue Essay.new
    @essay.studentname = session[:username]
    @essay.update_attributes(params[:essay])

    respond_to do |format|
      format.html { redirect_to student_url, notice: 'Essay saved.' }
      format.json { render json: {:status => 'saved'} }
    end
    
  end
=begin  
  def save_eval
    @essay = Essay.find(params[:id]) rescue Essay.new
    @essay.studentname = session[:username]
    @essay.update_attributes(params[:essay])

    respond_to do |format|
      format.html { redirect_to student_url, notice: 'Essay saved.' }
      format.json { render json: {:status => 'saved'} }
    end
    
  end
=end  
  
  def save_eval
    evals = EssayEval.find(params[:id])
    evals.score1 = params[:scorerange].to_f
    evals.score2 = 1-evals.score1

    evals.update_attributes(params[:essay_eval])
    
    respond_to do |format|
      format.html { redirect_to student_url(:mark_index => params[:mark_index]), notice: 'Essay saved.'  }
      format.json { render json: {:status => 'saved'} }
    end
    
  end
    
  def login 
      if params[:username] then
          session[:username] = params[:username]
          redirect_to student_url
      end    
  end
  
  def logout 
      session.delete :username
      session.delete :admin
      redirect_to login_url      
  end
  
  def showessay
      @essay = Essay.find(params[:id])
      eval1 = EssayEval.where(:essay1_id => params[:id]).all.map {|e| [e.pcomment1, e.ccomment1]}
      eval2 = EssayEval.where(:essay2_id => params[:id]).all.map {|e| [e.pcomment2, e.ccomment2]}      
      @evals = eval1 + eval2
  end
  
  
  def checkIfLoggedIn!
      if session.has_key? :username and not session[:username].nil?then
           return true
      else      
           redirect_to login_url
           return false
      end
  end
  
end
