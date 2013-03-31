class HomeController < ApplicationController
  def index
  end
  
  def student
      checkIfLoggedIn!
      @student = session[:username]   
      @assignment = Assignment.current_assignment
      puts(@assignment.id)
      @form_from_state = 'list'
      if(@assignment != nil) then
          case @assignment.state
             when "BUSY"
                 @essay = @assignment.essays.where(:studentname => @student).first
                 if @essay == nil 
                     @essay = @assignment.essays.new
                 end    
                 @form_from_state = 'enter'
             when "MARKING"
                 @form_from_state = 'mark'         
          end   
      end
  end
  
  def save
    checkIfLoggedIn!
    @essay = Essay.find(params[:id]) rescue Essay.new
    @essay.studentname = session[:username]
    @essay.update_attributes(params[:essay])

    redirect_to student_url, notice: 'Essay saved.' 
  end
  
  def login 
      if params[:username] then
          session[:username] = params[:username]
          redirect_to student_url
      end    
  end
  
  def logout 
      session.delete :username
      redirect_to login_url      
  end
  
  
  def checkIfLoggedIn!
      if session.has_key? :username then
           return true
      else
           redirect_to login_url
      end
  end
  
end
