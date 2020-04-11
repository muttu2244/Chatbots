## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Car Insurance

* greet
    - utter_greet
* affirm
    - utter_happy
* bot_challenge
    - utter_iamabot
* bot_challenge
    - utter_wheretobuy
* bot_challenge
    - utter_mandatory
* affirm
    - utter_insurancecost
* bot_challenge
    - utter_insurancecost
* affirm
    - utter_effect_insurance_rates
* deny
    - utter_goodbye
* goodbye
    - utter_goodbye
