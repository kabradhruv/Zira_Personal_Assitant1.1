import speech_recognition as sr
# sr.Microphone(device_index=2)
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# print(sr.Microphone.list_microphone_names())
