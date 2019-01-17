from flask import Flask, request,jsonify
import datetime

app = Flask(__name__)

#list of users
list_of_users =[
{'userid':1,'firstname':'Peter','lastname':'Pan', 'othername': 'Greg','email':'peter@gmail.com','phoneNumber':'0774985635'},
{'userid':2,'firstname':'Mary','lastname':'Jane', 'othername': 'Jay','email':'mary@gmail.com','phoneNumber':'0774985645'},
]

#list of incidents
list_of_incidents =[{'incidentid':1,
					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
					'createdBy':'Pan', 
					'type': 'red-flag',
					'location':'23.8,45.6',
 					'image':'image',
 					'video':'video',
 					'status':'investgation',
 					'comment':'comments'},

 					{'incidentid':2,
 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
 					'createdBy':'Pan', 
 					'type': 'red-flag',
 					'location':'23.8,45.6',
 					'image':'image',
 					'video':'video',
 					'status':'invesstgation',
 					'comment':'weired'},

 					{'incidentid':3,
 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
 					'createdBy':'Ben', 
 					'type': 'red-flag',
 					'location':'57.5,7.9',
 					'image':'image',
 					'video':'video',
 					'status':'invesstgation',
 					'comment':'weired'}
]


#display list
display_list =[]

#returns all the incidents
@app.route('/api/<version>/red-flags', methods = ['GET'])
def get_red_flags(version):
	 
	return jsonify({'status':200,'data':list_of_incidents})

#returns a specific red-flag
@app.route('/api/<version>/red-flags/<int:red_flag_id>', methods = ['GET'])
def get_one_red_flag(version,red_flag_id):
	try:
		incident = list_of_incidents[red_flag_id-1]  
	except IndexError:
		return jsonify({'status':404},{'error':'Incident not found'}), 404
	return jsonify({'data':incident,'status':200})


#creates a new incident
@app.route('/api/<version>/red-flags',methods = ['POST'])
def addred_flag(version):
	#counts the number of records present in the list
	incidentid = len(list_of_incidents)

	#returns the current date and time
	now = datetime.datetime.now()

	#values are entered from here
	incident = {'incidentid': incidentid+1,
				'createdOn':now,
				'createdBy':request.json['createdBy'],
				'type':request.json['type'],
				'Location':request.json['Location'],
				'image':'image',
				'video':'video',
				'status': 'Under Investgation',
				'comment':request.json['comment']
}

	#Record is added to the list
	list_of_incidents.append(incident)


	#the list contais the status code and "Created red-flag record" message
	display_list=[{'incidentid':incidentid+1,'message':'Created red-flag record'}]

	return jsonify({'data':display_list,'status':201}), 201


#edits the location of a particuler flag
@app.route('/api/<version>/red-flags/<int:red_flag_id>/location',methods = ['PATCH'])
def edit_red_flag_location(version,red_flag_id):

	try:
		#assigns a new locations value to a particuler 
		list_of_incidents[red_flag_id-1]['Location'] = request.json['Location']

		#contains the status and the message
		display_list=[{'incidentid':red_flag_id,'message':"Updated the red-flag record's location"}
		]
	#this exception is thrown if the item refered to does not exist
	except IndexError:
		return jsonify({'status':404},{'error':'Incident not found'}), 404
	return jsonify({'data':display_list,'status':201}), 201


#edits the comment
@app.route('/api/<version>/red-flags/<int:red_flag_id>/comment',methods = ['PATCH'])
def edit_red_flag_comment(version,red_flag_id):
	
	try:
		#assigns a new value to the comments of the selelcted incident
		list_of_incidents[red_flag_id-1]['comment'] = request.json['comment']

		display_list=[ {'incidentid':red_flag_id,'message':"Updated the red-flag record's comment"}
		]

	#this exception is thrown if the item refered to does not exist
	except IndexError:
		return jsonify({'status':404},{'error':'Incident not found'}), 404
	return jsonify({'data':display_list,'status':201}), 201


#deletes the incident
@app.route('/api/<version>/red-flags/<int:red_flag_id>',methods = ['DELETE'])
def delete_red_flag(version, red_flag_id):

	try:
		#gets the incident to be deleted
		del(list_of_incidents[red_flag_id-1])

		display_list=[ {'incidentid':red_flag_id,'message':"red-flag record has been deleted"}
		]

	#this exception is thrown if the incident refered to does not exist
	except IndexError:
		return jsonify({'status':404},{'error':'Incident not found'}), 404
	return jsonify({'data':display_list,'status':201}), 201

if __name__ == "__main__":
	app.run(debug=True)
