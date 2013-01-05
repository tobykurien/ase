# Testing the peer marker

require 'net/http'


students = %w( s1 s2 s3 )
teacher = 'admin1'

threads = []

for student in students
  threads << Thread.new(student) { |s|
      Net::HTTP.start('127.0.0.1', 8081) { |http|
         req = Net::HTTP::Post.new('/login')
         req.set_form_data({'username'=> s, 'bsubmit'=>'Login'}, ';')
      
         res = http.request(req)
         if res.body.include? "<title>Menu - KhanAcademy</title>"
            puts "Logged in: #{s}" 
         else
            puts "ERROR: #{res.body}"
         end
         
         res = http.get('/englishessay/')
         if res.body.include? "<title>Assignment - "
            puts "#{s} ready to enter essay" 
         else
            puts "ERROR: #{res.body}"
         end
      }
  }
end


threads.each { |aThread|  aThread.join }
