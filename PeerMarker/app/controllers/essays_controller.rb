class EssaysController < ApplicationController
  # GET /essays
  # GET /essays.json
  def index
    assignment_id = params[:assignment_id]
    @essays = Essay.where(:assignment_id => assignment_id)

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @essays }
    end
  end

  # GET /essays/1
  # GET /essays/1.json
  def show
    @essay = Essay.find(params[:id])
    @assignment = Assignment.find(params[:assignment_id])
    
    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @essay }
    end
  end

  # GET /essays/new
  # GET /essays/new.json
  def new
    @assignment = Assignment.find(params[:assignment_id])
    @essay = Essay.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @essay }
    end
  end

  # GET /essays/1/edit
  def edit
    @assignment = Assignment.find(params[:assignment_id])
    @essay = Essay.find(params[:id])
  end

  # POST /essays
  # POST /essays.json
  def create
    newEssay = params[:essay]
    newEssay[:assignment_id] = params[:assignment_id]
    @essay = Essay.new(newEssay)
    
    respond_to do |format|
      if @essay.save
        format.html { redirect_to assignment_essay_url(@essay.assignment_id, @essay.id), notice: 'Essay was successfully created.' }
        format.json { render json: @essay, status: :created, location: @essay }
      else
        format.html { render action: "new" }
        format.json { render json: @essay.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /essays/1
  # PUT /essays/1.json
  def update
    @assignment = Assignment.find(params[:assignment_id])
    @essay = Essay.find(params[:id])
    
    respond_to do |format|
      if @essay.update_attributes(params[:essay])
        format.html { redirect_to assignment_essay_url(@essay.assignment_id, @essay.id), notice: 'Essay was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @essay.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /essays/1
  # DELETE /essays/1.json
  def destroy
    @essay = Essay.find(params[:id])
    @essay.destroy

    respond_to do |format|
      format.html { redirect_to assignment_essays_path(params[:assignment_id]) }
      format.json { head :no_content }
    end
  end
end
