require 'test_helper'

class AssignmentTest < ActiveSupport::TestCase
   test "should rank assignments correctly" do
      # todo - test ranking here
      marking = Marking.new
      marking.populateMarking assignments(:one)
      marking.doscoring assignments(:one)
      
      assert true
   end
end
