# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import SlotSet


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSayName(Action):

  def name(self) -> Text:
    return "action_say_name"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    name = tracker.get_slot("name")
    if not name:
      dispatcher.utter_message(text="I don't know your name.")
    else:
      dispatcher.utter_message(text=f"Your name is {name}.")
    return []

class ActionCheckReaction(Action):
  def name(self) -> Text:
    return "action_check_reaction"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    response = tracker.latest_message['text']

    entities = tracker.latest_message['entities']

    slots = {}
    for entity in entities:
        slots[entity['entity']] = entity['value']
    name = tracker.get_slot("reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check if the person is showing no reaction and has no normal breathing.")
    else:
      dispatcher.utter_message(text="What do you do now?")
    return[]

class ActionCheckCPR(Action):

  def name(self) -> Text:
    return "action_check_cpr"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    missing = False
    name = tracker.get_slot("reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check if the person is showing no reaction and has no normal breathing.")
      missing = True
    name = tracker.get_slot("cpr")
    if not name:
      dispatcher.utter_message(text="You forgot to start giving CPR with chest compression and ventilation in a ratio of 30:2.")
    if missing:
      dispatcher.utter_message(text="Please go on.")
    else:
      dispatcher.utter_message(text="That's correct. Please go on.")
    return[SlotSet("reaction", "no reaction"), SlotSet("cpr", "giving cpr")]

class ActionCheckMeasures(Action):

  def name(self) -> Text:
    return "action_check_measures"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    missing = False
    name = tracker.get_slot("reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check if the person is showing no reaction and has no normal breathing.")
      missing = True
    name = tracker.get_slot("cpr")
    if not name:
      dispatcher.utter_message(text="You forgot to start giving CPR with chest compression and ventilation in a ratio of 30:2.")
      missing = True
    name = tracker.get_slot("measures")
    if not name:
      dispatcher.utter_message(text="You forgot to establish enhanced measures.")
      missing = True
    name = tracker.get_slot("medication_access")
    if not name:
      dispatcher.utter_message(text="You forgot to establish access for medication.")
      missing = True
    name = tracker.get_slot("advanced_ventilation")
    if not name:
      dispatcher.utter_message(text="You forgot to establish advanced ventilation measures.")
      missing = True
    name = tracker.get_slot("defibrillation")
    if not name and not missing:
      dispatcher.utter_message(text="Quite well, but you forgot to place and connect the defibrillation electrodes.")
    elif not name:
      dispatcher.utter_message(text="You forgot to place and connect the defibrillation electrodes.")
    elif not missing:
      dispatcher.utter_message(text="Good. Go on please.")
    else:
      dispatcher.utter_message(text="Go on please.")
    return[SlotSet("reaction", "no reaction"), SlotSet("cpr", "giving cpr"), SlotSet("measures", "enhanced measures"), SlotSet("medication_access", "medication"), SlotSet("advanced_ventilation", "ventilation"), SlotSet("defibrillation", "defibrillation")]

class ActionCheckECG(Action):

  def name(self) -> Text:
    return "action_check_ecg"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    missing = False
    name = tracker.get_slot("reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check if the person is showing no reaction and has no normal breathing.")
      missing = True
    name = tracker.get_slot("cpr")
    if not name:
      dispatcher.utter_message(text="You forgot to start giving CPR with chest compression and ventilation in a ratio of 30:2.")
      missing = True
    name = tracker.get_slot("measures")
    if not name:
      dispatcher.utter_message(text="You forgot to establish enhanced measures.")
      missing = True
    name = tracker.get_slot("medication_access")
    if not name:
      dispatcher.utter_message(text="You forgot to establish access for medication.")
      missing = True
    name = tracker.get_slot("advanced_ventilation")
    if not name:
      dispatcher.utter_message(text="You forgot to establish advanced ventilation measures.")
      missing = True
    name = tracker.get_slot("defibrillation")
    if not name:
      dispatcher.utter_message(text="You forgot to place and connect the defibrillation electrodes.")
      missing = True
    name = tracker.get_slot("ecg")
    if not name:
      dispatcher.utter_message(text="You forgot emergency ECG diagnostics.")
      missing = True
    name = tracker.get_slot("medication_administration")
    if not name:
      dispatcher.utter_message(text="You forgot to administrate medication.")
      missing = True
    name = tracker.get_slot("shock")
    if not name:
      dispatcher.utter_message(text="You forgot to administrate shock if necessary.")
      missing = True
    if missing:
      dispatcher.utter_message(text="Do you remember the medication dosage?")
    else:
      dispatcher.utter_message(text="That's correct. Do you remember the medication dosage?")
    return[SlotSet("reaction", "no reaction"), SlotSet("cpr", "giving cpr"), SlotSet("measures", "enhanced measures"), SlotSet("medication_access", "medication"), SlotSet("advanced_ventilation", "ventilation"), SlotSet("defibrillation", "defibrillation"), SlotSet("ecg", "emergency ECG diagnostics"), SlotSet("medication_administration", "medication administration"), SlotSet("shock", "shock administration")]

class ActionCheckDosage(Action):

  def name(self) -> Text:
    return "action_check_dosage"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    name = tracker.get_slot("epinephrine")
    if not name:
      dispatcher.utter_message(text="The correct dosage is 1 mg epinephrine.")
    name = tracker.get_slot("rinse")
    if not name:
      dispatcher.utter_message(text="That's right, and remember to rinse with at least 20 mL NaCl 0.9% and elevate the extremity when administering peripherally.")
    else:
      dispatcher.utter_message(text="That's right.")
    return[]

class ActionResetAllSlots(Action):

  def name(self) -> Text:
    return "action_reset_all_slots"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    dispatcher.utter_message("All slots reset.")

    return [AllSlotsReset()]