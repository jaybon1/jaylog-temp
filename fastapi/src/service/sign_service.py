
from datetime import datetime
import bcrypt
from sqlalchemy.orm import Session

from dto import sign_dto
from entity.user_entity import UserEntity
from util import functions

USER_ID_EXIST_ERROR = {"code": 1, "message": "이미 존재하는 아이디 입니다."}
ID_NOT_EXIST_ERROR = {"code": 2, "message": "가입되지 않은 아이디 입니다."}
DELETED_USER_ERROR = {"code": 3, "message": "삭제된 유저 입니다."}
PASSWORD_INCORRECT_ERROR = {"code": 4, "message": "비밀번호가 틀립니다."}
INTERNAL_SERVER_ERROR = {"code": 99, "message": "서버 내부 에러 입니다."}


def sign_in(reqDTO: sign_dto.ReqSignIn, db: Session):
    userEntity: UserEntity = db.query(UserEntity).filter(
        UserEntity.id == reqDTO.id).first()

    # 아이디가 없을경우
    if userEntity == None:
        return functions.res_generator(status_code=400, error_dict=ID_NOT_EXIST_ERROR)

    # 아이디가 삭제된 경우
    if userEntity.delete_date != None:
        return functions.res_generator(status_code=400, error_dict=DELETED_USER_ERROR)

    # 비밀번호가 틀릴 경우
    if not bcrypt.checkpw(reqDTO.password.encode("utf-8"), userEntity.password.encode("utf-8")):
        return functions.res_generator(status_code=400, error_dict=PASSWORD_INCORRECT_ERROR)

    # 정상
    

    pass


def sign_up(reqDTO: sign_dto.ReqSignUp, db: Session):
    userEntity: UserEntity = db.query(UserEntity).filter(
        UserEntity.id == reqDTO.id).first()

    if userEntity != None:
        return functions.res_generator(status_code=400, error_dict=USER_ID_EXIST_ERROR)

    db_user = UserEntity(
        id=reqDTO.id,
        password=bcrypt.hashpw(
            reqDTO.password.encode("utf-8"), bcrypt.gensalt()),
        simple_desc=reqDTO.simpleDesc if reqDTO.simpleDesc else "한 줄 소개가 없습니다.",
        profile_image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
        role="BLOGER",
        create_date=datetime.now()
    )

    try:
        db.add(db_user)
        db.flush()
    except Exception as e:
        db.rollback()
        print(e)
        return functions.res_generator(status_code=500, error_dict=INTERNAL_SERVER_ERROR)
    finally:
        db.commit()

    db.refresh(db_user)

    return functions.res_generator(status_code=201, content=sign_dto.ResSignUp(idx=db_user.idx))
