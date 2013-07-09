module AssignmentsHelper
   def show_started(startdatetime)
      if startdatetime ==nil then
         result = "Not started"         
      else
          result = startdatetime.strftime "%Y-%m-%d %H:%M"
      end
      return result
   end
   
   
end
