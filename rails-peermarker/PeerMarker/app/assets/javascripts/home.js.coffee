# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://jashkenas.github.com/coffee-script/
class HomeClass

  constructor: ->
    @lastSaved = ""
    @timeout = null

  save: (url, form, button, callback)->
    self = this
    successCB = (data, textStatus, jqXHR) ->
      $('#'+button).text "Saved"
      $('#'+button).attr 'disabled','disabled'
      Home.timeout = null
      if callback
        callback()
      
      
    self.dataToSave = $('form').serialize()

    $.ajax {
          type: "POST",
          url: url,
          data: self.dataToSave,
          success: successCB,
          dataType: 'json'
        }
        
   save_eval: (url,mark_index=null) ->
     callback = () -> 
        location.href = '/student?mark_index='+mark_index
     callback = null if mark_index == null
     @save(url, 'essay_eval','save-button', callback)       

   save_enter: (url) ->
     @save(url, 'essay','save-button')


root = exports ? this
root.Home = new HomeClass()

$(document).ready ->
  mark_dirty = () -> 
    $('#save-button').text "Save"
    $('#save-button').removeAttr 'disabled'
    if Home.timeout == null
      Home.timeout = ()-> 
        $('#save-button').click()
      setTimeout Home.timeout, 5000
    
  $('.autosave').keydown mark_dirty  

  if $('#countdown').attr('data-timeremaining')
    t= countdown 'countdown', 0, $('#countdown').attr('data-timeremaining')
    $('#countdown').html(t)
    $('#countdown').counter({})

