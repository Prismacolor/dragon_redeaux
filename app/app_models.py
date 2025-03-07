from pydantic import BaseModel
from typing import Optional, Union, Literal

class ModelInputs(BaseModel):
    """
    Pydantic model for validating input data
    """

    gender: Literal['male', 'female']
    estimated_age: Literal['juvenile', 'adult', 'elder']
    color_of_scales: str
    color_of_eyes: str
    color_of_wings: str
    est_body_length: float
    shape_of_snout: str
    shape_of_teeth: str
    scales_present: str
    scale_texture: str
    body_texture: str
    snout_length: float
    shape_of_body: str
    wingspan: float
    number_of_limbs: int
    facial_spikes: str
    frilled: str
    length_of_horns: str
    shape_of_horns: str
    shape_of_tail: str
    loc_of_sighting: str
    aggressiveness: float
    flight_speed: float
    is_venomous: str
    breathing_fire_observed: str
    observed_by: Optional[str] = None
    year_observed: Optional[int] = None


class PredictionResponse(BaseModel):
    """
    Response model for the prediction
    """

    prediction: str
    input_data: dict