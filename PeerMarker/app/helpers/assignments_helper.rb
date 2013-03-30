module AssignmentsHelper
   def show_started(startdatetime)
      result = startdatetime
      if startdatetime ==nil then
         result = "Not started"         
      end
      return result
   end
   
end
