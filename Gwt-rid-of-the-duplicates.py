student_data = {'id1':
                {'name':['zain'],
                 'class':['vii'],
                 'subject_integration':['English,math,science']
                 },
                    'id2':
                            {'name':['shubha mam'],
                            'class':['vi'],
                            'subject_integration':['English,math,science']
                            },

            'id3':
                            {'name':['Tawseef'],
                            'class':['vii'],
                            'subject_integration':['English,math,science']
                            },


            'id4':
                            {'name':['Muzaffar'],
                            'class':['vii'],
                            'subject_integration':['English,math,science']
                            },

            }


result={}

for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)



