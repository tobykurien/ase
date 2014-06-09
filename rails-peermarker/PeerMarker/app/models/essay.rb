class Essay < ActiveRecord::Base
  belongs_to :assignment
  attr_accessible :essay_text, :grade, :score, :studentname, :assignment_id
end
