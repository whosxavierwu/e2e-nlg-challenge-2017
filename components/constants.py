PAD_TOKEN = '<blank>'
BOS_TOKEN = '<s>'
EOS_TOKEN = '</s>'
UNK_TOKEN = '<unk>'
# we dont need to use the value of fields "name" and "near"
NAME_TOKEN = '<name>'
NEAR_TOKEN = '<near>'

PAD_ID = 0
BOS_ID = 1
EOS_ID = 2
UNK_ID = 3

START_VOCAB = [PAD_TOKEN,
               BOS_TOKEN,
               EOS_TOKEN,
               UNK_TOKEN,
               ]

# todo need to change the mr_fields to about 200.
MR_FIELDS = ["name", "familyFriendly", "eatType", "food", "priceRange", "near", "area", "customer rating"]
MR_KEYMAP = dict((key, idx) for idx, key in enumerate(MR_FIELDS))
