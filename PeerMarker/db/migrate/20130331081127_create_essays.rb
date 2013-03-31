class CreateEssays < ActiveRecord::Migration
  def change
    create_table :essays do |t|
      t.string :studentname
      t.string :essay_text
      t.decimal :score
      t.decimal :grade
      t.references :assignment

      t.timestamps
    end
    add_index :essays, :assignment_id
  end
end
