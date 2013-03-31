class CreateEssayEvals < ActiveRecord::Migration
  def change
    create_table :essay_evals do |t|
      t.string :studentname
      t.integer :assignment_id
      t.integer :essay1_id
      t.string :essay2_id
      t.decimal :score1
      t.decimal :score2

      t.timestamps
    end
  end
end
