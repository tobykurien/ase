class EssayEval < ActiveRecord::Base
  attr_accessible :assignment_id, :essay1_id, :essay2_id, :score1, :score2, :student_name, :pcomment1, :pcomment2, :ccomment1, :ccomment2
end
