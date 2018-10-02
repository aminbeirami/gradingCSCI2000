import pandas as pd

student_list_dir = 'directory.csv'
grades_dir = 'a2_grades.txt'

def return_actual_list():
	student_list_dataframe = pd.read_csv(student_list_dir, header =1)
	student_list_dataframe = student_list_dataframe.rename(columns = {'Email':'email'})
	student_list_dataframe = student_list_dataframe.drop(columns = ['Term Code','CRN','Course Code', '#'])
	return student_list_dataframe	

def read_grades():
	score_dataframe = pd.read_csv(grades_dir, sep="|", header=0)
	score_dataframe.replace(' ','',regex=True,inplace=True)
	score_dataframe = score_dataframe.rename(columns = lambda x: x.strip())
	return score_dataframe

def list_of_grades(score_dataframe,info_dataframe):
	grades_dataframe = pd.merge(info_dataframe,score_dataframe, on = 'email', how = 'left')
	return grades_dataframe

grades = read_grades()
names = return_actual_list()
grades_dataframe = list_of_grades(grades,names)
grades_dataframe.to_csv('detailed_grades.csv')