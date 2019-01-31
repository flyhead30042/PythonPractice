from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from yaml import load, dump
from swagger_parser import SwaggerParser






if __name__ == "__main__":

    base_path = os.path.dirname(os.path.abspath(__file__))
    swagger_yaml_path = base_path +"\swagger.yml"
    parser = SwaggerParser(swagger_path=swagger_yaml_path)
    print ("swagger_yaml_path =" + swagger_yaml_path)
    # print(parser.specification)
    # print("======================")
    # print(parser.definitions_example)