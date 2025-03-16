import { create } from "zustand";

// Define the store state type
interface StoreState {
  // Example state properties
  count: number;
  items: string[];

  // Example actions
  increment: () => void;
  decrement: () => void;
  addItem: (item: string) => void;
  removeItem: (index: number) => void;
  reset: () => void;
}

// Create the store
const useStore = create<StoreState>((set) => ({
  // Initial state
  count: 0,
  items: [],

  // Actions that modify state
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),

  addItem: (item) =>
    set((state) => ({
      items: [...state.items, item],
    })),

  removeItem: (index) =>
    set((state) => ({
      items: state.items.filter((_, i) => i !== index),
    })),

  reset: () => set({ count: 0, items: [] }),
}));

export default useStore;
