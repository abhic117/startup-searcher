from dataclasses import dataclass
from typing import Optional

@dataclass
class Startup:
    name: Optional[str] = None
    overview: Optional[str] = None
    location: Optional[str] = None
    industry: Optional[str] = None
    stage: Optional[str] = None
    team: Optional[str] = None
    funding: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def toString(self):
        return f'''Startup: {self.name}
Overview: {self.overview}
Location: {self.location}
Industry: {self.industry}
Stage: {self.stage}
Team: {self.team}
Funding: {self.funding}
Description: {self.description}
URL: {self.url}
'''