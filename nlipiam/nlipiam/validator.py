# A custom validator to provide the profile information
#
# This is where the additional claims for JWTs or /userinfo may be added
#
# TOM: note, overriding get_claim_dict(self, request) may prove fruitful as well.

from oauth2_provider.oauth2_validators import OAuth2Validator

class CustomOAuth2Validator(OAuth2Validator):

    # TOM: this adds additional claiims for OpenID/JWT generation
    def get_additional_claims(self, request):
        user = request.user
        print(f"USER:{user}")
        print(f"USER.EMAIL:{user.email}")
        return {
            'sub' : str(user.id), # subject claim (required)
            'email': user.email,
            'given_name' : user.first_name,
            'family_name' : user.last_name,
            'preferred_username' : user.username,
            # add other claims as needed
        }

    # TOM: this method adds the claims for the /userinfo request
    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        user = request.user
        claims["preferred_username"] = user.get_username()
        claims["fullname"] = user.get_full_name()
        claims["given_name"] = user.first_name
        claims["family_name"] = user.last_name
        return claims

    
            
