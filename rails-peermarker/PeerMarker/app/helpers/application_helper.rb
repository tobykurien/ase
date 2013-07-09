module ApplicationHelper
   def loggedin?
      session.has_key? :username
   end



end
