from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserConfig(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  userId = db.Column(db.String, unique=True, nullable=False)
  layersNum = db.Column(db.Integer, unique=False, nullable=True)
  neuronsNum = db.Column(db.Integer, unique=False, nullable=True)
  optimizer = db.Column(db.String, unique=False, nullable=True)
  lossFunc = db.Column(db.String, unique=False, nullable=True)
  alpha = db.Column(db.Float, unique=False, nullable=True)
  weightsId = db.Column(db.String, unique=True, nullable=True)

  def to_json(self):
    return {
      "id": self.id,
      "userId": self.userId,
      "layersNum": self.layersNum,
      "neuronsNum": self.neuronsNum,
      "optimizer": self.optimizer,
      "lossFunc": self.lossFunc,
      "alpha": self.alpha,
      "weightsId": self.weightsId
    }
  
class Weights(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  configId = db.Column(db.String, unique=True, nullable=False)
  jsonFile = db.Column(db.String, unique=False, nullable=False)
  binFile = db.Column(db.LargeBinary, unique=False, nullable=False)

  def to_json(self):
    return {
      "id": self.id,
      "configId": self.configId,
      "jsonFile": self.jsonFile,
      "binFile": self.binFile
    }
  