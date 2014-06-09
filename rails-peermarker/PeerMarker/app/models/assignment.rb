class Assignment < ActiveRecord::Base
    attr_accessible :description, :duration, :startdatetime, :title, :state
    validate :check_state
    has_many :essays

    def self.current_assignment_id
        list = Assignment.where ({:state => ["BUSY","MARKING"]})
        return list[0].id rescue nil
    end 
    
    def self.current_assignment
        return Assignment.find(current_assignment_id) rescue nil
    end
        
    def check_state
        current = Assignment.current_assignment_id
        if (["BUSY","MARKING"].include? state) and (current != nil) and (current != id) then
            errors.add(:state, "can't change the state")
        end
    end
    
   
end
