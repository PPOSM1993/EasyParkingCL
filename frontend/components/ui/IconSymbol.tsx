// IconSymbol.tsx

import AntDesign from '@expo/vector-icons/AntDesign'; // 👈 Ya lo tienes
import MaterialIcons from '@expo/vector-icons/MaterialIcons';
import { OpaqueColorValue, StyleProp, TextStyle } from 'react-native';

type IconSymbolName =
  | 'house.fill'
  | 'paperplane.fill'
  | 'login.circle.fill'
  | 'adduser.fill'; // Agrega aquí los que necesites

// Mapear nombres simbólicos a nombres reales e íconos de librerías
const MAPPING: Record<
  IconSymbolName,
  {
    name: string;
    family: 'MaterialIcons' | 'AntDesign';
  }
> = {
  'house.fill': { name: 'home', family: 'MaterialIcons' },
  'paperplane.fill': { name: 'send', family: 'MaterialIcons' },
  'login.circle.fill': { name: 'login', family: 'AntDesign' },
  'adduser.fill': { name: 'adduser', family: 'AntDesign' },
};

export function IconSymbol({
  name,
  size = 24,
  color,
  style,
}: {
  name: IconSymbolName;
  size?: number;
  color: string | OpaqueColorValue;
  style?: StyleProp<TextStyle>;
}) {
  const icon = MAPPING[name];
  if (!icon) return null;

  const { name: iconName, family } = icon;

  const IconComponent = family === 'AntDesign' ? AntDesign : MaterialIcons;

  return <IconComponent name={iconName} size={size} color={color} style={style} />;
}
