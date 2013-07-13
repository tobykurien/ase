module ApplicationHelper
   def loggedin?
      session.has_key? :username or session.has_key? :admin
   end



end
