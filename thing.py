from debug import dbg

class Thing:
    def __init__(self, ID):
        self.id = ID
        self.weight = 0.0
        self.volume = 0.0
        self.location = None
        self.fixed = False
        self.short_desc = 'need_short_desc'
        self.long_desc = 'need_long_desc'
        # dictionary mapping verb strings to functions:
        self.verb_dict = {"look":           self.look_at,
                          "examine":        self.look_at,
                          "take":           self.take,
                          "get":            self.take,
                          "drop":           self.drop
                          }
        self.contents = None        # None - only Containers can contain things

    def set_weight(self, grams):
        if (grams < 0):
            dbg.debug("Error: weight cannot be negative")
            raise
        else:
            self.weight = grams

    def set_volume(self, liters):
        if (liters < 0):
            dbg.debug("Error: volume cannot be negative")
            raise
        else:
            self.volume = liters

    def set_location(self, containing_object):
        self.location = containing_object

    def fix_in_place(self, error_message):
        self.fixed = True
        self.error_message = error_message

    def unfix(self):
        self.fixed = False

    def set_description(self, s_desc, l_desc):
        self.short_desc = s_desc
        self.long_desc = l_desc

    def new_verb(self, verb, func):
        self.verb_dict[verb] = func

    def heartbeat(self):
        pass

    def emit(self, message):
        """Write a message to be seen by creatures holding this Thing or in the same room"""
        # pass message to containing object, if it can receive messages
        holder = self.location
        if not holder: 
            return 
        if hasattr(holder, 'perceive'):
            # immeidate container can see messages, probably a creature/player
            dbg.debug("creature holding this object is: " + holder.id)
            holder.perceive(message)
        # now get list of recipients (usually creatures) contained by holder (usually a Room)
        recipients = {x for x in holder.contents if hasattr(x, 'perceive') and (x is not self)}
        dbg.debug("other creatures in this room include: " + str(recipients))
        for recipient in recipients:
            recipient.perceive(message)
        
        # dbg.debug("object "+self.id+" emitted message '"+message+" but nobody was around to hear it.")

    def look_at(self, cons, oDO, oIDO):  # print out the long description of the thing
        cons.write(self.long_desc)

    def move_to(self, cons, oDO, oIDO):
        if self.fixed:
            cons.write(self.error_message)
        else:
            if self.location != None:
                self.location.extract(self)
            oDO.insert(self)

    def take(self, cons, oDO, oIDO):
        if not self.fixed and oDO != self:
            self.move_to(cons, cons.user, oIDO)
            cons.write("You take the %s." % self.id)

    def drop(self, cons, oDO, oIDO):
        if not self.fixed and oDO != self:
            self.move_to(cons, cons.user.location, oIDO)
            cons.write("You drop the %s." % self.id)

