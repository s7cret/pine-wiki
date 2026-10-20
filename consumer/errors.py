class Diagnostic(Exception):
    def __init__(self,category,message,rule_id=None,span=None,reason=None,evidence_refs=None,decision_ref=None,issue_refs=None):
        self.data={'category':category,'message':message,'rule_id':rule_id,'source_span':span,
                   'reason':reason,'evidence_refs':evidence_refs or [],'decision_ref':decision_ref,'issue_refs':issue_refs or []}
        super().__init__(message)


def invalid(message,rule='rule.grammar',span=None):
    raise Diagnostic('LANGUAGE_INVALID',message,rule,span)
