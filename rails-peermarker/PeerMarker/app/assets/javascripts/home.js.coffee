# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://jashkenas.github.com/coffee-script/
class Home

  constructor: ->
    @lastSaved = ""

  save: (url)->
    self = this
    successCB = (data, textStatus, jqXHR) ->
      $('#save-button').text "Saved"
      $('#save-button').attr 'disabled','disabled'
      
      
    self.dataToSave = $('#essay').serialize()

    $.ajax {
          type: "POST",
          url: url,
          data: self.dataToSave,
          success: successCB,
          dataType: 'json'
        }

root = exports ? this
root.Home = new Home()

$(document).ready ->
  $('#essay_essay_text').keydown () -> 
    $('#save-button').text "Save"
    $('#save-button').removeAttr 'disabled'
    timeout = ()-> 
      $('#save-button').click()
    setTimeout timeout, 5000

  t= countdown 'countdown', 0, $('#countdown').attr('data-timeremaining')
  $('#countdown').html(t)
  $('#countdown').counter({})

