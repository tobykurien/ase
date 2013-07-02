class CreateEssays < ActiveRecord::Migration
  def change
    create_table :essays do |t|
      t.string :studentname
      t.string :essay_text
      t.decimal :score, :precision => 5, :scale => 2, :default => 0.00
      t.decimal :grade, :precision => 5, :scale => 2, :default => 0.00
      t.references :assignment

      t.timestamps
    end
    add_index :essays, :assignment_id
  end
end
