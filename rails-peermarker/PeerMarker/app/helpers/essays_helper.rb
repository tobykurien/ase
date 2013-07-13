module EssaysHelper
  def make_short(text)
     return text[0,10] + " ..." unless text.nil?
     return "" if text.nil?
  end
  
  def not_marked(mark)
      if mark == nil then
         return "Not Marked"
      else
         return mark
      end       
  end
end
