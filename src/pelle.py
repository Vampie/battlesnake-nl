from .brein import SlangenBrein

# Pelle is very hungry all the time
class Pelle(SlangenBrein):
  
  def hungry(self):
    return True

  def get_value(self, direction):
    val = super().get_value(direction)
    neighbour = self.board.neighbour(self.my_head(), direction)  
    # pelle is smart, she also checks if neighbour cell *might* be occupied next round
    if neighbour is not None:
      if neighbour.can_be_occupied_in_next_round:
        val = val - 100
      if neighbour.is_food:
        val = val + 100
    return val

  def value_for_cell(self, cell):
        if cell.is_snake():
            return -5
        elif cell.is_food():
                return 15
        else:
                return 1
        
  def potential_next_moves(self, snake):
      kop = snake.segmenten[0]
      Debug.log_with_action(kop.position_string(), 'Head + potential moves')
      mogelijke_cellen = []
      c = self.buur_links(kop)
      if c is not None:
        mogelijke_cellen.append(MogelijkeSlang(c.x, c.y))
      c = self.buur_rechts(kop)
      if c is not None:
        mogelijke_cellen.append(MogelijkeSlang(c.x, c.y))
      c = self.buur_boven(kop)
      if c is not None:
        mogelijke_cellen.append(MogelijkeSlang(c.x, c.y))
      c = self.buur_onder(kop)
      if c is not None:
        mogelijke_cellen.append(MogelijkeSlang(c.x, c.y))
      for i in mogelijke_cellen:
        Debug.log(i.position_string())
      return mogelijke_cellen



class MogelijkeSlang(Cel):

    def is_vrij(self):
        return False

    def als_letter(self):
        return '?'