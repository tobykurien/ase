class Marking

  def populateMarking(assignment)

      EssayEval.where(:assignment_id => assignment.id).delete_all
      essays = assignment.essays
      essayCount = essays.length

      repetitions = 3
      maxCombinations = factorial(essayCount)/factorial(essayCount-2)/factorial(2)
      if maxCombinations< essayCount*repetitions then
         repetitions = (maxCombinations / essayCount).floor.to_i
      end   
      pairs = assignPairs(essayCount, repetitions)   
      essayCount.times.each do |i|
         repetitions.times.each do |j|
            index = i*repetitions+j
            
            ee = EssayEval.new
            ee.essay1_id = essays[pairs[index][0]].id
            ee.essay2_id = essays[pairs[index][1]].id
            ee.studentname = essays[i].studentname
            ee.assignment_id = assignment.id
            ee.save
         end
      end   
     
  end

  def assignPairs(essaysCount, numberToSelect)
    result = []
    essayIndex = 0

    while essayIndex < essaysCount do
        numberIndex = 0
        while numberIndex < numberToSelect do
            a = rand(essaysCount)
            b = rand(essaysCount)
            if not (result.include? [a,b]) and not (result.include? [b,a]) and not a==b and not a==essayIndex and not b==essayIndex then
                result.append([a,b])
                numberIndex += 1
            end    
        end        
        essayIndex += 1
    end    
    return result
  end  

  def factorial(n)
    n.zero? ? 1 : n * factorial(n - 1)
  end

  def doscoring(assignment)
    essays = Essay.where(:assignment_id => assignment).to_a
    ids = essays.map {|i| i['id'] }

    essay_evals = EssayEval.where(:assignment_id => assignment).to_a
    a = Matrix.zero(essay_evals.count)
    
    essay_evals.each do |i|
      row = ids.index(i['essay1_id'])
      col = ids.index(i['essay2_id']) 
      s1 = i['score1'] 
      s2 = i['score2']
      s1 = 0.5 if s1.nil?
      s2 = 0.5 if s2.nil?
      a[row,col] = s1
      a[col,row] = s2
    end

    c = colley(a)
    c1 = standardize(c)
    puts ">>>>>>>>>>>>>>>", c1.inspect

    essays.each do |e|
      puts c1[0,ids.index(e['id'])].to_f
      e.score = c1[0,ids.index(e['id'])].to_f
      e.grade = nil
      e.save!
    end

  end
end  
  
class MarkProgress
   attr_accessor :studentname, :pairsmarked, :total
end
