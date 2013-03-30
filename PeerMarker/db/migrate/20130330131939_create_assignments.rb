class CreateAssignments < ActiveRecord::Migration
  def change
    create_table :assignments do |t|
      t.string :title
      t.string :description
      t.integer :duration
      t.datetime :startdatetime

      t.timestamps
    end
  end
end
