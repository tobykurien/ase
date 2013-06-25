class CreateEssayEvals < ActiveRecord::Migration
  def change
    create_table :essay_evals do |t|
      t.string   :studentname
      t.integer  :assignment_id
      t.integer  :essay1_id
      t.integer  :essay2_id
      t.decimal  :score1
      t.decimal  :score2
      t.string   :pcomment1
      t.string   :ccomment1
      t.string   :pcomment2
      t.string   :ccomment2
      t.timestamps
    end
  end
end
