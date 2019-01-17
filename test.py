import unittest
import run
import json
from flask_testing import TestCase
import datetime

class TestMainFlask(TestCase):

	def create_app(self):
		return run.app

	#checks that the number of incidents is more than 0
	def test_get_red_flags(self):
		response = self.client.get('/api/v1/red-flags')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(len(data['data']),0)

	#checks that a specific incident can be returned
	def test_get_one_red_flag(self):
		response = self.client.get('/api/v1/red-flags/2')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'incidentid':2,
					 					'createdOn':'Thu, 29 Nov 2018 11:46:35 GMT',
					 					'createdBy':'Pan', 
					 					'type': 'red-flag',
					 					'location':'23.8,45.6',
					 					'image':'image',
					 					'video':'video',
					 					'status':'invesstgation',
					 					'comment':'weired'})


	#tests that a new incident can be added
	def test_addred_flag(self):

		now_test = datetime.datetime.now()
		response = self.client.post('/api/v1/red-flags',
                                        content_type='application/json',
                                        data=json.dumps(dict(createdBy = 'Bob',
                                        					 type='Red-Flag',
                                        					 Location='45,67',
                                        					 comment='Weired'
                                        					 )))


		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['data'],[{'incidentid':4,'message':'Created red-flag record'}])


	#tests that the location is correctly edited
	def test_edit_red_flag_location(self):
			response = self.client.patch('/api/v1/red-flags/3/location',
	                                     content_type='application/json',
	                                     data=json.dumps(dict(Location='7,7')))



			data = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			self.assertEqual(data['data'],[{'incidentid':3,'message':"Updated the red-flag record's location"}])


	#tests that the comment is correctly edited
	def test_edit_red_flag_comment(self):
			response = self.client.patch('/api/v1/red-flags/3/comment',
	                                     content_type='application/json',
	                                     data=json.dumps(dict(comment='comment edited')))



			data = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			self.assertEqual(data['data'],[{'incidentid':3,'message':"Updated the red-flag record's comment"}])


	#tests that an incident is correctly deleted
	def test_delete_red_flag(self):
		response = self.client.delete('/api/v1/red-flags/4')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['data'],[{'incidentid':4,'message':'red-flag record has been deleted'}])





if __name__ == '__main__':
	unittest.main()

