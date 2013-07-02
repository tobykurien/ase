require 'test_helper'

class AssignmentTest < ActiveSupport::TestCase
   test "should rank assignments correctly" do
      # todo - test ranking here
      Marking.new.populateMarking assignments(:one)
      
      assert true
   end
end
