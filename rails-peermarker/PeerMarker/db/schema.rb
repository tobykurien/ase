# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20130402223001) do

  create_table "assignments", force: true do |t|
    t.string   "title"
    t.string   "description"
    t.integer  "duration",      default: 15,    null: false
    t.datetime "startdatetime"
    t.string   "state",         default: "NEW", null: false
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "essay_evals", force: true do |t|
    t.string   "studentname"
    t.integer  "assignment_id"
    t.integer  "essay1_id"
    t.integer  "essay2_id"
    t.decimal  "score1",        precision: 5, scale: 2, default: 0.0
    t.decimal  "score2",        precision: 5, scale: 2, default: 0.0
    t.string   "pcomment1"
    t.string   "ccomment1"
    t.string   "pcomment2"
    t.string   "ccomment2"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "essays", force: true do |t|
    t.string   "studentname"
    t.string   "essay_text"
    t.decimal  "score",         precision: 5, scale: 2, default: 0.0
    t.decimal  "grade",         precision: 5, scale: 2, default: 0.0
    t.integer  "assignment_id"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  add_index "essays", ["assignment_id"], name: "index_essays_on_assignment_id", using: :btree

end
