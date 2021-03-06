import sys

# Sybmols, please try to find the right group and add symbols sorted by name
symbols = (
    # Arrows
    'Downwards Arrow',
    'Left Right Arrow',
    'Leftwards Arrow Over Rightwards Arrow',
    'Leftwards Arrow',
    'North West Arrow',
    'Rightwards Arrow Over Leftwards Arrow',
    'Rightwards Arrow',
    'Up Down Arrow',
    'Upwards Arrow',

    # Currencies
    'Colon Sign',
    'Euro Sign',
    'New Sheqel Sign',
    'Pound Sign',

    # Hearts
    'Black Heart Suit',
    'White Heart Suit',

    # Greek
    'Greek Capital Letter Alpha',
    'Greek Capital Letter Beta',
    'Greek Capital Letter Gamma',
    'Greek Capital Letter Delta',
    'Greek Capital Letter Epsilon',
    'Greek Capital Letter Zeta',
    'Greek Capital Letter Eta',
    'Greek Capital Letter Theta',
    'Greek Capital Letter Iota',
    'Greek Capital Letter Kappa',
    'Greek Capital Letter Lamda',
    'Greek Capital Letter Mu',
    'Greek Capital Letter Nu',
    'Greek Capital Letter Xi',
    'Greek Capital Letter Pi',
    'Greek Capital Letter Rho',
    'Greek Capital Letter Sigma',
    'Greek Capital Letter Tau',
    'Greek Capital Letter Upsilon',
    'Greek Capital Letter Phi',
    'Greek Capital Letter Chi',
    'Greek Capital Letter Psi',
    'Greek Capital Letter Omega',
    'Greek Small Letter Alpha',
    'Greek Small Letter Beta',
    'Greek Small Letter Gamma',
    'Greek Small Letter Delta',
    'Greek Small Letter Epsilon',
    'Greek Small Letter Zeta',
    'Greek Small Letter Eta',
    'Greek Small Letter Theta',
    'Greek Small Letter Iota',
    'Greek Small Letter Kappa',
    'Greek Small Letter Lamda',
    'Greek Small Letter Mu',
    'Greek Small Letter Nu',
    'Greek Small Letter Xi',
    'Greek Small Letter Pi',
    'Greek Small Letter Rho',
    'Greek Small Letter Sigma',
    'Greek Small Letter Tau',
    'Greek Small Letter Upsilon',
    'Greek Small Letter Phi',
    'Greek Small Letter Chi',
    'Greek Small Letter Psi',
    'Greek Small Letter Omega',

    # Math
    'Dot Operator',
    'Intersection',
    'Larger Than or Equal To',
    'Less-Than or Equal To',
    'Not Equal To',
    'Union',

    # Misc
    'Pile of Poo',

    # Smilies
    'Black Smiling Face',
    'Smiling Face with Halo',
    'Smiling Face with Heart-Shaped Eyes',
    'Smiling Face with Horns',
    'Smiling Face with Open Mouth and Smiling Eyes',
    'Smiling Face with Smiling Eyes',
    'Smiling Face with Sunglasses',
    'White Smiling Face',

    # Stars
    'Black Star',
    'White Star',
    'Star of David',
    'Star and Crescent',
)

if sys.version_info[:2] > (3, 6):
    symbols += (
        'Bitcoin Sign',
    )
