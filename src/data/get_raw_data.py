# -*- coding: utf-8 -*-
import json
import os
import logging

# getting root directory
project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
# read kaggle API token and create enviornment variables
api_file_path = '/Users/pojashad/.kaggle/kaggle.json'
with open(api_file_path) as f:
    kaggle_token = json.load(f)
    # environment variable for kaggle authentication
    os.environ["KAGGLE_USERNAME"] = kaggle_token['username']
    os.environ["KAGGLE_KEY"] = kaggle_token['key']


from kaggle.api.kaggle_api_extended import KaggleApi

def main(project_dir):
    '''
    main method
    '''
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    # file name : check from the competition data page
    train_file_name = 'train.csv'
    test_file_name = 'test.csv'

    # file paths
    raw_data_path = os.path.join(project_dir,'data','raw')
    
    # extract data
    api = KaggleApi()
    api.authenticate()
    api.competition_download_file(competition='titanic', file_name=train_file_name, path=raw_data_path, force=True)
    api.competition_download_file(competition='titanic', file_name=test_file_name, path=raw_data_path, force=True)
    logger.info('downloaded raw training and test data')


if __name__ == '__main__':
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # call the main
    main(project_dir)
