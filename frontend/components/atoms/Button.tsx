import { Text, TouchableOpacity } from 'react-native';

interface Props {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
}

export default function Button({ title, onPress, variant = 'primary' }: Props) {
  const styles = variant === 'primary' ? 'bg-blue-600 text-white' : 'bg-gray-200 text-black';
  return (
    <TouchableOpacity onPress={onPress} className={`px-4 py-2 rounded ${styles}`}>
      <Text className="text-center font-semibold">{title}</Text>
    </TouchableOpacity>
  );
}
