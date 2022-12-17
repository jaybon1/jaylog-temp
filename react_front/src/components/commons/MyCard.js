import React from "react";
import { Card, Col, Image, InputGroup, Row } from "react-bootstrap";
import NoimageImg from "assets/img/no-image.png";
import LikeImg from "assets/img/like.svg";

const MyCard = ({ post }) => {
  return (
    <Col>
      <Card className="m-3">
        <Card.Img
          variant="top"
          src={post.thumbnail ? post.thumbnail : NoimageImg}
        />
        <Card.Body>
          <Card.Title>{post.title}</Card.Title>
          <Card.Text>{post.summary}</Card.Text>
          <small className="text-muted mx-3 mb-2">{post.createDate}</small>
        </Card.Body>
        <Card.Footer>
          <Row>
            <Col>
              <InputGroup>
                <Image
                  className="ratio ratio-1x1 rounded-circle me-2"
                  src={post.writer.profileImage}
                  style={{ width: "24px", height: "24px" }}
                  alt="profileImage"
                />
                <strong>{post.writer.id}</strong>
              </InputGroup>
            </Col>
            <Col>
              <InputGroup>
                <Image src={LikeImg} width="15" />
                <span className="mx-2 fs-6 text-black-50 fw-light">
                  {post.likeCount}
                </span>
              </InputGroup>
            </Col>
          </Row>
        </Card.Footer>
      </Card>
    </Col>
  );
};

export default MyCard;
