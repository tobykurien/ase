require 'eventmachine'

require 'rails'
require 'active_record'

$LOAD_PATH << Dir.pwd
require 'protected_attributes'
require "app/models/essay"

class Connection < EventMachine::Connection
  def post_init
    puts "-- someone connected to the echo server!"
  end

  def set_server(server)
    @server = server
  end

  def receive_data data
    @server.receive_data self.object_id, data
  end

  def unbind
    @server.unbind self.object_id
    puts "-- someone disconnected from the echo server!"
  end
end

class Server
  def receive_data id, data
    @conns[id].send_data "Echo #{data}"
    @conns[id].close_connection_after_writing
  end
  
  def run
    @conns = {}
    ActiveRecord::Base.establish_connection(
      :adapter => "sqlite3",
      :database => "/db/test.sqlite3"
    )
  
    EventMachine.start_server "127.0.0.1", 8081, Connection do |conn|
      @conns[conn.object_id] = conn
      conn.set_server self
    end
    
    puts "PeerMarker essays server started"
  end
  
  def unbind(id)
    @conns.delete id
  end
end

# Note that this will block current thread.
EventMachine.run {
  s = Server.new
  s.run
}
