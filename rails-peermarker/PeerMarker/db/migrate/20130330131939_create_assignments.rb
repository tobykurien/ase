class CreateAssignments < ActiveRecord::Migration
  def change
    create_table :assignments do |t|
      t.string :title
      t.string :description
      t.integer :duration, :null => false, :default => 15
      t.datetime :startdatetime
      t.string :state, :null => false, :default => 'NEW'

      t.timestamps
    end
  end
end
