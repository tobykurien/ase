# Testing the peer marker

require 'net/http'


students = %w( s1 s2 s3 )
teacher = 'admin1'

threads = []

for student in students
  threads << Thread.new(student) { |s|
      res = Net::HTTP.post_form(URI.parse('http://localhost:8081/login'),
                                          {'username'=> s, 'bsubmit'=>'Login'})
      if res.body.include? "<title>Menu - KhanAcademy</title>"
         puts "Logged in: #{s}" 
      else
         puts "ERROR: #{res.body}"
      end
      
      res = Net::HTTP.get(URI.parse('http://localhost:8081/englishessay/'))
      if res.include? ""
         puts "#{s} ready to enter essay" 
      else
         puts "ERROR: #{res.body}"
      end
  }
end


threads.each { |aThread|  aThread.join }
