require 'test_helper'

class EssayTest < ActiveSupport::TestCase
   test "essay saves correctly" do
     e = essays(:one)
     e.score = 0.5
     e.grade = 1.5
     e.save!
     
     assert_equal 1.5, e.grade, "Grade not saved correctly"          
     assert_equal 0.5, e.score, "Score not saved correctly"
   end
end
