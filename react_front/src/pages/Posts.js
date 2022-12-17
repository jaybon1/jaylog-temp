import CommonLayout from "components/layouts/CommonLayout";
import React from "react";
import { CardGroup, Container } from "react-bootstrap";

const Posts = () => {
  return (
    <CommonLayout isNavbar={true}>
      <Container className="mt-3">
        <CardGroup className="row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xxl-4">
          {"카드 리스트"}
        </CardGroup>
      </Container>
    </CommonLayout>
  );
};

export default Posts;
