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
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20130331081127) do

  create_table "assignments", :force => true do |t|
    t.string   "title"
    t.string   "description"
    t.integer  "duration",      :default => 15,    :null => false
    t.datetime "startdatetime"
    t.string   "state",         :default => "NEW", :null => false
    t.datetime "created_at",                       :null => false
    t.datetime "updated_at",                       :null => false
  end

  create_table "essays", :force => true do |t|
    t.string   "studentname"
    t.string   "essay_text"
    t.decimal  "score"
    t.decimal  "grade"
    t.integer  "assignment_id"
    t.datetime "created_at",    :null => false
    t.datetime "updated_at",    :null => false
  end

  add_index "essays", ["assignment_id"], :name => "index_essays_on_assignment_id"

end
