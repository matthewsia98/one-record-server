from typing import Optional, Set

from pydantic import BaseModel, Field

from app.models.common import IRI


class ErrorDetail(BaseModel):
    iri: IRI
    code: str
    message: Optional[str] = None
    property: Optional[IRI] = None
    resource: Optional[IRI] = None


class Error(BaseModel):
    iri: IRI
    title: str
    error_detail: Set[ErrorDetail] = Field(default_factory=set)

    @classmethod
    def create_error(
        cls,
        iri: IRI,
        title: str,
        detail: ErrorDetail,
    ) -> Error:
        return Error(
            iri=iri,
            title=title,
            error_detail=set([detail]),
        )

    @classmethod
    def create_error_with_info(
        cls,
        iri: IRI,
        title: str,
        detail_iri: IRI,
        code: str,
        detail_message: str,
    ) -> Error:
        return Error(
            iri=iri,
            title=title,
            error_detail=set(
                [
                    ErrorDetail(
                        iri=detail_iri,
                        code=code,
                        message=detail_message,
                    )
                ]
            ),
        )
